t1 = sigmoid(0.5) # Applying a sigmoid activation function to a constant value of 0.5
t2 = t1 * 0.8 # Multiplying the output of the sigmoid by another constant of 0.8
t3 = -t2 + torch.tensor([[-0.7, 0]])  # Adding another constant tensor [-0.7] to the output of the sigmoid multiplied by a constant value of 0.8. The result is another constant value of 0.95
