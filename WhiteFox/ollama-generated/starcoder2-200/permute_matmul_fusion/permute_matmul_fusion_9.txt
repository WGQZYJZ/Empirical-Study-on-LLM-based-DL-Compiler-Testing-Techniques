
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()

    def forward(self, x1, x2):
        v1 = torch.randn(4, 5) 
        v2 = torch.nn.functional.relu(v1 + 3.)
        v3 = torch.nn.functional.leaky_relu(x2 / v2)
        return (
            torch.bmm(
                x1[:, None].permute((0, 2, 1)).contiguous(), 
                #torch.matmul(
                #    x1[:, None], 
                #    #x1[None] 
                #).squeeze(-1), 
                # torch.nn.functional.linear(v3, self.linear.weight, self.linear.bias),
                v3
            )
        )

# Initializing the model
m  = Model()

# Inputs to the model
x1 = torch.randn(200)[:, None]
x2 = torch.randint(-4., 5.) + x1.abs()

