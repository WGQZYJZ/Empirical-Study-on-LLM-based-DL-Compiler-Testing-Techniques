
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()

    def forward(self, x1):
        t0 = torch.relu(x1) # 2-dim input with 3 classes
        t1 = torch.cat([t0[:, :2], self.t2, t0[: , -1]], dim=1) # Concatenate the first two dimensions of a 2d tensor and a 4d one along axis 1.
        return torch.nn.functional.linear(t1, self.linear.weight, self.linear.bias).view(-1, 3).permute([0, -1])


t2 = torch.randn(4, 2) # A 4d 2-dimension tensor as another input.
self.t2 = t2; # Save this tensor for later re-use.
self.linear = torch.nn.Linear(5, 3) # A 1D tensor used as a weight tensor of the linear layer.

