# Public reproduction constraint, not the lost 16 nm sign-off constraint.
create_clock -name core_clk -period 10.000 [get_ports clk]
set_clock_uncertainty 0.20 [get_clocks core_clk]
set_input_delay 0.50 -clock core_clk [remove_from_collection [all_inputs] [get_ports clk]]
set_output_delay 0.50 -clock core_clk [all_outputs]
