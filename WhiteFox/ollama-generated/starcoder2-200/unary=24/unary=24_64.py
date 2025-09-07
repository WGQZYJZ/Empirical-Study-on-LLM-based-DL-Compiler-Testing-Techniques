t1 = 1 / (input_tensor + epsilon)  # Apply the Reciprocal function to the input tensor and add a small constant epsilon, where the default value is set to 2e-5.
t2 = t1 * 0.9  # Multiply the output of the reciprocal by a constant 0.9
