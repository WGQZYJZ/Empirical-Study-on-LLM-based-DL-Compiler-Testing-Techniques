
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear = torch.nn.Linear(2, 2)

    def forward(self, x1):
        t1 = torch.nn.functional.dropout(x1, p=0.5, inplace=False, training=True)
        # Erase the dropout call of linear as the replacement will invoke random functions instead
        gm.graph.erase_node(gm.get_call_to_function(torch.nn.functional.linear))
        v2 = torch.rand_like(t1, t1.dtype)  # This line is not replaced. It is a valid PyTorch function call that does not need to be optimized.
        return v2


# Test Case: model with an op that can't be analyzed and an unmodified tensor as input (as it is not used by any op).
class MyModule(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear = torch.nn.Linear(2, 3)

    def forward(self, x1):
        v1 = torch.pow(x1, 2.0) + torch.exp(-x1) + 10 * torch.sin(x1)
        v2 = torch.sin(v1)
        return self.linear(v2)


# Initializing the model
m = MyModule()
gm.optimize_model(m, fallback_random=True)
x1 = torch.randn(1, 3, requires_grad=False, device='cuda')
