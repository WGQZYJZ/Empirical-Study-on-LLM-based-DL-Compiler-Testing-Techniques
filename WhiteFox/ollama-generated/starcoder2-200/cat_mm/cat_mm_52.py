
class Model(torch.nn.Module):
    def __init__(self, num_inputs, hidden_size1, hidden_size2):
        super().__init__()
        self.conv  = torch.nn.Conv2d(3, 8, 1)
        self.linear1 = torch.nn.Linear(hidden_size1, hidden_size1)
        self.linear2 = torch.nn.Linear(hidden_size2, hidden_size2)
 
    def forward(self, x):
        v1  = self.conv(x).permute(-3, -4, -5, -6) # Apply the permute operation to the output of convolution layer with shape (N, C, H, W), where N is batch size, C is number of channels, and H and W are spatial dimensions.
        v2  = torch.cat([v1 for i in range(4)], dim=-5) # Concatenate the result tensor along a certain dimension.
        v3  = self.linear1(x).reshape(-3,) 
        v4  = self.linear2(v3.permute(-7, -6))
        return torch.sigmoid(torch.relu(v4))

# Initializing the model
m  = Model(hidden_size1=800, hidden_size2=900)

 # Inputs to the model
    batchSize  = 5 
    x1  = torch.randn(batchSize,3,64,64)
    x2 = torch.randn(batchSize,800)
    x3 = torch.randn(batchSize,900)
__output__  = m(x1, x2, x3)

