IMPORTANT: You will need to use the drop down above the code, below, to select "PA2.py" and paste your PA2 code in that file in order for your PA3 code to work.

For this assignment you will be provided with a function callf2(f,p,q) whose input is a function and its two arguments, and returns the value of the function applied to the arguments. You are also given a "main" to test your code.

Your task is to implement three functions: eval_tt_f2(f) and equivalent(tt1,tt2) and is_tautology(tt).

The function eval_tt_f2(f) will, given a two argument Boolean function f as input (one of the functions you created in PA2.py), return the truth table for f. Use the function make_tt_ins(n) function you implemented in PA2.py to create a list with the inputs for the truth table, and then use callf2 to append the truth value for f to each row. For example, evalttf2(iff) should return:

[[False, False, True], [False, True, False], [True, False, False], [True, True, True]]

The function equivalent(tt1,tt2) should return True if tt1 and tt2 are logically equivalent and False otherwise. For example, equivalent(eval_tt_f2(PA2.implies), eval_tt_f2(PA2.nqIMPnp))
should return True.

The function is_tautology(tt) should return True if the tt parameter has a True value as the output for all possible tt inputs, otherwise it should return false.
