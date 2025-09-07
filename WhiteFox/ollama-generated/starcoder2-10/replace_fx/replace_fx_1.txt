
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear  = torch.nn.Linear(2, 1000)

    def forward(self, x): 
        v  = x.permute([0, 3, 1, 2])
        t1 = torch.nn.functional.dropout(v, p=0.75, training=True) # Apply dropout to the permuted tensor.
        v2 = torch.nn.functional.linear(t1, self.linear.weight, bias=None).view(-1, 3) 
        return v2

# Initializing the model
m  = Model()


