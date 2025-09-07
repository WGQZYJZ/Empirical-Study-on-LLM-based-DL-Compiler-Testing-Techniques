
class Model(torch.nn.Module):
    def __init__(self, opt=None):
        super().__init__()
        self.linear = torch.nn.Linear(2, 2)

    @torch.no_grad()
    def forward(self, x1, return_loss=False):
        v1 = x1.permute(0, 2, 1)
        v2 = torch.nn.functional.linear(v1, self.linear.weight, self.linear.bias)
        if return_loss:
            return v2, v1
        else:
            loss = torch.nn.functional.mse_loss(x1, v2)
            mae = torch.abs(v2 - x1).mean()
            return loss + mae

# Initializing the model
m  = Model()
m.to('cuda')


