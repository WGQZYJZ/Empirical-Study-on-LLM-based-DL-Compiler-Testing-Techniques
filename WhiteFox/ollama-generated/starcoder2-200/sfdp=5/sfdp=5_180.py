t1 = torch.tanh(w1 * a1 + b1) # Apply an activation function to the dot product between the input and weight matrix a1 with bias term b1. The output is then multiplied by another input.
t2 = w2 * t1 + b2  # Apply another activation function, and then multiply the output of this first activation function by another matrix w2.  Add the bias term to the output of that multiplication
