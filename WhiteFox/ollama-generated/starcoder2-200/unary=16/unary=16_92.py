
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear = torch.nn.Linear(512 * 7 * 7, 4096)

    def forward(self, x1):
        v1 = self.linear(x1)
        v2 = F.relu(v1)
	return v2

# Initializing the model
m = Model()


# Inputs to the model
x1 = torch.randn(4096).view(-1, 512*7*7)

 # Outputs of the model. Please also provide the output from `F.relu(v1)` as the expected output for this input tensor (`F.relu(v1) = __expected_output__`)
__output__  = m(x1)
