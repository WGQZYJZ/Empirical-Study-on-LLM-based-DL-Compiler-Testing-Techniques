t1 = t1 * t3  # Apply the output of the sigmoid function to the output of the linear transformation
t2 = torch.exp(-t1)  # Apply the exponential function to the negative output of the sigmoid function
t3 = t2 / max(t2)  # Divide each value in t2 by the maximal element in t2, and store them in t3
