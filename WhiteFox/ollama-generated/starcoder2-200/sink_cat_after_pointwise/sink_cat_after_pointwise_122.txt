
class Model(torch.nn.Module):
    def __init__(self, input_dim=2048):
        super().__init__()
        self.conv1 = torch.nn.Conv2d(input_dim, 365, kernel_size=[7, 7], stride=(2, 2), padding=(3, 3), groups=1)
        self.conv2 = torch.nn.Conv2d(365, 840, kernel_size=[1, 1])

    def forward(self, x):
        v1 = torch.cat([x, x], dim=1)
        v2 = v1.view(-1, 900) # This reshaped tensor is only used as an input for the ReLU function.
        v3 = torch.relu(v2)

        return v3


# Initializing the model and its inputs
x = torch.randn([16, 478], dtype=torch.float64) # A valid 900D vector
model_with_tensor_inputs  = Model(input_dim=len(x))
output  = model_with_tensor_inputs(x).data

