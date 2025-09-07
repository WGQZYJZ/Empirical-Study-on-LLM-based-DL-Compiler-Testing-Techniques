
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear1 = torch.nn.Linear(2, 4)

    def forward(self, x1, x2):
        t1 = x1.permute(0, 2, 1)
        t3 = x2.permute(0, 2, 1)
        t2 = self.linear1(t3)

        t5 = torch.bmm(t1, t2)
        return t5


# Initializing the model
m  = Model()

# Inputs to the model
x1 = torch.randn(1, 2, 4) # Shape: [1 x 4 x 3] or [batch_size x 3 x 4]. If the first tensor is larger than the second one, you need to swap their shape order before feeding them into the model
x2 = torch.randn(1, 3, 5) # Shape: [1 x 3 x 5] or [batch_size x 5 x 3]. If the first tensor is larger than the second one, you need to swap their shape order before feeding them into the model
