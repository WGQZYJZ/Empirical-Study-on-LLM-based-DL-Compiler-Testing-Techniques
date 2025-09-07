

class ConcatModel(torch.nn.Module):
    def __init__(self, size=92348756):
        super().__init__()
        self.size = size
    
    def forward(self, *inputs):
        out  = torch.cat([i for i in inputs], dim=1)
        out2 = out[:, :self.size]
        out3 = out2[:, :self.size]
        return [torch.cat((out, out3), dim=1)]


# Initializing the model<|end_of_model|>
m  = ConcatModel(984)

