def test_firstprogram(Setup_teardown):
    calc=Setup_teardown
    # Perform calculation: 1 + 2 =
    calc.child_window(auto_id="num1Button", control_type="Button").click()
    calc.child_window(auto_id="plusButton", control_type="Button").click()
    calc.child_window(auto_id="num2Button", control_type="Button").click()
    calc.child_window(auto_id="equalButton", control_type="Button").click()

    # Access result display
    display = calc.child_window(auto_id="CalculatorResults", control_type="Text")

    # Extract text
    result_text = display.window_text()  # or display.iface_value.CurrentValue

    # Clean up text (it usually starts with "Display is ")
    value = result_text.replace("Display is ", "").strip()
    assert value=="3", "addition value dosent match"

