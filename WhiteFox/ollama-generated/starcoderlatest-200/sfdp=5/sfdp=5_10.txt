
class SelfAttention(torch.nn.Module):
    def __init__(self, k_model=128, q_model=128):
        super().__init__()
 
        self.q = torch.nn.Conv2d(1, k_model, kernel_size=(3, 3), stride=(2, 2)) # Convolve each query in the input feature map with a fixed-size convolutional layer to create a sequence of queries, where the number of filters is equal to the dimensionality of the last hidden state of the previous convolutional layer
        self.v = torch.nn.Conv2d(1, k_model, kernel_size=(3, 3), stride=(2, 2)) # Convolve each value in the input feature map with a fixed-size convolutional layer to create a sequence of values, where the number of filters is equal to the dimensionality of the last hidden state of the previous convolutional layer
 
        self.fc = torch.nn.Linear(k_model * 2, k_model) # Linearly transform a flattened representation of the queries and values into a single, fixed-size representation
        self.dropout = torch.nn.Dropout(p=0.5)
 
    def forward(self, x1):
        v1 = self.v(x1)
        qk = self.q(x1).unsqueeze(dim=-2)  # Unsqueze to expand the last dimension (from 3d to 4d)
        output = torch.bmm(qk, v1.transpose(-2, -1)) + 0.
        output = self.dropout(output) # Apply dropout after the batch-wise linear transformation
        output = self.fc(output).view(x1.size()[0], x1.size()[1], -1)
 
        return output


# Inputs to the model
input_feature = torch.randn(2, 3, 64, 64)
