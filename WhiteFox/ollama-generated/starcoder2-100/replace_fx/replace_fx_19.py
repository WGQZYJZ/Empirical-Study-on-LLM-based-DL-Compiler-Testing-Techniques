class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear  = torch.nn.Linear(2, 2)

    def forward(self, x1):
         v1  = torch.nn.functional.dropout(x1, p=0.5) # Apply dropout to the input tensor with probability 0.5
         v2  = torch.nn.functional.dropout(v1, p=0.3)
         return self.linear(v2)
