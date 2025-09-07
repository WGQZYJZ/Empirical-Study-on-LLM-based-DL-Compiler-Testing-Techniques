t_linear = torch.nn.Linear(in_features=dimension, out_features=hidden_size) # Linear layer for input tensor and dimension output_dimensions are different.
t_activation = torch.nn.ReLU()  # Activation function of ReLU type
t_fc = torch.nn.Linear(in_features=hidden_size, out_features=output_dimensions) # Final linear layer to obtain the result.
