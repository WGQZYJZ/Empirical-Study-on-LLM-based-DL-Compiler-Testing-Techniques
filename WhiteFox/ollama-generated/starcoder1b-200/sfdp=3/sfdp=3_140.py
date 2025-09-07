
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv1 = torch.nn.Conv2d(3, 8, 1)  # input_tensor to filter_matrix
        self.conv2 = torch.nn.Conv2d(3, 4, 1)  # input_tensor to output_tensor

    def forward(self, x):
        filter_matrix = x.matmul(self.conv2.weight.unsqueeze(-1).unsqueeze(-1))  # Compute the dot product between x and the weight matrix
        filter_matrix = self.conv1(filter_matrix)  # Apply a conv to the output of the previous layer
        filter_matrix = filter_matrix.squeeze()  # Convert it back into one-dimensional
        filter_matrix = filter_matrix * 0.25  # Multiply by a factor

        dropout_q = F.softmax(filter_matrix, dim=-1)  # Softmax the dot product of the weight matrix and compute the dropout output
        value = x.matmul(self.conv1.weight.unsqueeze(-1).unsqueeze(-1))  # Compute the dot product between x and the input tensor
        value = self.conv2(value)  # Apply a conv to the output of the previous layer
        value = value.squeeze()  # Convert it back into one-dimensional
        value = value * 0.25  # Multiply by a factor

        return F.dropout(value, p=dropout_p)  # Use dropout to calculate the dot product between the weight matrix and the input


# Initializing the model
m = Model()

# Inputs to the model
x1 = torch.randn(1, 3, 64, 64)
