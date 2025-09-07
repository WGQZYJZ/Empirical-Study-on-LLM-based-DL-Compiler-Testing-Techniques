
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()

    def forward(self, x1, y2):  # In fact it should not be necessary to include both inputs in the model.
        # This is only for testing
        v1 = torch.randn(x1)  # or torch.ones(x1), or even torch.full([batch_size], 3.).to(x1.device)
        t2  = x1.permute(-1, -2).expand(v1.shape[0], -1, v1.shape[-1]) 
        t3  = y2.permute(-1, -2).expand(v1.shape[0], -1, v1.shape[-1])
        return torch.bmm(t2 + t3)

# Initializing the model
m  = Model()


# Inputs to the model
a1 = x1.clone()
a2 = y2.clone()
__output___ = m(a1, a2).sum().item() # Here is an important step for debugging. 

