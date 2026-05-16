# Testing Patterns

Use these snippets as compact examples of shape and intent. Prefer the target project's existing tests when they differ.

## TypeScript / JavaScript

Behavior-first tests should make setup, action, and assertion obvious.

```ts
describe("parseAmount", () => {
  it("rejects negative values", () => {
    expect(() => parseAmount("-1")).toThrow("amount must be positive");
  });

  it("returns normalized cents for valid input", () => {
    expect(parseAmount("12.34")).toEqual({ cents: 1234 });
  });
});
```

For async code, await the behavior under test rather than relying on timing.

```ts
it("shows the saved state after submit", async () => {
  render(<SettingsForm save={saveSettings} />);

  await userEvent.click(screen.getByRole("button", { name: "Save" }));

  expect(await screen.findByText("Saved")).toBeVisible();
});
```

## Foundry / Solidity

Name tests after the behavior or failure mode. Assert reverts, events, balances, and state at the contract boundary.

```solidity
function test_RevertWhen_CallerIsNotOwner() public {
    vm.prank(alice);
    vm.expectRevert(Ownable.Unauthorized.selector);

    vault.withdraw(1 ether);
}

function test_DepositUpdatesBalance() public {
    vm.deal(alice, 1 ether);
    vm.prank(alice);

    vault.deposit{value: 1 ether}();

    assertEq(vault.balanceOf(alice), 1 ether);
}
```

## Swift

Prefer deterministic dependencies for async work, clocks, persistence, and platform boundaries.

```swift
func testLoadProfileReturnsCachedValue() async throws {
    let store = InMemoryProfileStore(profile: .fixture(name: "Ada"))
    let service = ProfileService(store: store)

    let profile = try await service.loadProfile()

    #expect(profile.name == "Ada")
}
```

With XCTest, keep the same arrange-act-assert shape.

```swift
func testValidatorRejectsEmptyEmail() {
    let validator = EmailValidator()

    XCTAssertThrowsError(try validator.validate(""))
}
```

## Anti-Patterns

- Testing private helpers directly when public behavior covers the same path.
- Mocking internal calls instead of asserting observable behavior.
- Adding large snapshots for dynamic UI or noisy serialized objects.
- Creating broad fixtures that hide the important input.
- Weakening assertions just to make a failing test pass.
