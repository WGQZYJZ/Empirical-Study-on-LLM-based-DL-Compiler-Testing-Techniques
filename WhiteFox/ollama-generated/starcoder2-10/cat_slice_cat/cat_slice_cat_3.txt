
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
    def forward(self, x1, y1):
        t1 = torch.cat([x1, y1], dim=0)
        return t1


# Initializing the model<|end_of_model|>
m  = Model()
__inputs_to_the_model__ = [
    torch.randn(1234567890, 3), 
    torch.randn(9000000000, 3)]
