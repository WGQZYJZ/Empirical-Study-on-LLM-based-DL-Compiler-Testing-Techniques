

class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()

    def forward(self, x1):

        def linear(x):
            return torch.nn.functional.linear(x)
        
        return torch.nn.functional.dropout(torch.rand_like(x1), p=0.5)(
                torch.nn.functional.linear(torch.nn.functional.relu(
                    torch.nn.functional.gelu(
                        linear(x1), inplace=True
                    ))))

