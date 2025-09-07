
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()

        self.conv1 = torch.nn.Conv2d(3, 6, 5)
        self.conv2 = torch.nn.Conv2d(6, 16, 5)

    def forward(self, x): 
        x = F.max_pool2d(F.relu(self.conv1(x)), (2, 2))
        x = F.max_pool2d(F.relu(self.conv2(x)), 2)

        return torch.flatten(x, 1).to_dense()


# Initializing the model
m = Model()


# Inputs to the model
input = torch.rand(50, 3, 480, 640) # input tensors should not be reshaped as 1D tensors.

# Outputs from the model with original implementation (without applying the optimization)
outputs_org = m(input)


# Inputs to the optimized model
input2 = torch.rand(50, 3, 480, 640) # input tensors should not be reshaped as 1D tensors.

# Outputs from the optimized model after applying the optimization 
outputs_new = m(input2)

