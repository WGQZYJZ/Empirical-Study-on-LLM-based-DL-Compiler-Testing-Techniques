
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear  = torch.nn.Linear(2, 2)

    def forward(self, x1): 
        v3  = torch.randn(50*4, 69*30).long()
        v7  = torch.LongTensor()
        t2 = (v7, v3)
        t21 = torch.nn.functional.linear(t2[0], self.linear.weight, self.linear.bias, t2[1]) # the permute() call may be invoked after
        return v5 # this line of the model may contain a non-validated torch.permute() call


# Initializing the model
m  = Model()

