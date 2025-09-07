
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear = torch.nn.Linear(3, 8)
 
    def forward(self, x1, other): # Passing the `other` tensor as a keyword argument in this line is OK
        v1  = self.linear(x1)
        v2  = v1 + other # Add another tensor to the output of the linear transformation
        v3  = torch.nn.functional.relu(v2) 
        return v3

# Initializing and compiling the model
m = Model()
m = m.cuda() if args['cuda'] else m
m = nn.DataParallel(m, device_ids=[0]) if len(args['gpus']) > 1 else m

