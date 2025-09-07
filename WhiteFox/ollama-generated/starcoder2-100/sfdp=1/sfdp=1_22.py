a  = torch.nn.Conv1d(a, b, 3).div(c).relu() # Convolutional layer with kernel size three and output dimension four
a2 = a * 0.5 # Multiplication by 0.5
a4 = torch.nn.AvgPool1d(a2, 4).add_(-0.5)  # Apply average pooling to the input tensor by dividing its elements with two
