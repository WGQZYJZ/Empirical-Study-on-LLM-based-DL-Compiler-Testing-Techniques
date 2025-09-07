
class Model(torch.nn.Module):
    def __init__(self, dim=30):
        super().__init__()

        self.linear1 = torch.nn.Linear(dim // 2 + 1, dim)

    def forward(self, x):
        # Input shape: [batch_size, timesteps]
        batch, timesteps = x.shape[:2]
        
        # Generate a uniform random tensor
        w1 = self._generate_tensor(x.device).expand(*x.shape, 1).uniform_()

        # Concatenate the input with a singleton axis and generate the output
        out = torch.cat([w1 * x, x], dim=-1)
        
        return torch.nn.functional.linear(out, self.linear1.weight, self.linear1.bias), w1

    @staticmethod
    def _generate_tensor(device):
        return torch.randn((2 ** 5) // 4).to(device)


# Initializing the model
m = Model()

# Inputs to the model
x = torch.rand([3, 7]) # [batch size, timesteps]
__output__  = m(x)