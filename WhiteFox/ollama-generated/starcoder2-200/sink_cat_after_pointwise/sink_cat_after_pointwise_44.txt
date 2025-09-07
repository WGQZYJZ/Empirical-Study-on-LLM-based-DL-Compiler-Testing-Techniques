
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()

    def forward(self, x1, x2):
        v = torch.cat([x1 + 10 * x2], dim=1) # Concatenate tensors along a dimension
        v = v.view(-1, 50)  # Reshape the concatenated tensor
        v = torch.relu(v)    # Apply pointwise ReLU to the reshaped tensor
        return v

m = Model()

x1 = torch.randn([4, 2]) + 1 # Input tensors of shape [batch size x input dimension] (e.g., 30 samples each containing 10 channels)
x2 = torch.randn(50).view(-1, 1) + 1 # A single input tensor with shape [input dimension] 
