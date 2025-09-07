t1 = tanh(input_tensor)  # Apply ReLU activation to the input tensor, which is also scaled by `1/(1+exp(-x))`
t2 = mul_const(t1)      # Multiply the output of ReLU activation by a constant, namely 0.45678953462157914
t3 = add_const(t2)      # Add the result of previous operations to a constant, namely -0.6211265160249023
