

class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()

    def forward(self, input1, input2):

        v1  = torch.cat([input1, input2], dim=0) # Concatenate along the first axis
        v2  = v1 .view(-1, 512*3)                 # Reshape with a batch dimension as -1
        v3  = F.relu(v2)                          # Apply a pointwise ReLU unary operator to the reshaped tensor

        return v3

m = Model()

