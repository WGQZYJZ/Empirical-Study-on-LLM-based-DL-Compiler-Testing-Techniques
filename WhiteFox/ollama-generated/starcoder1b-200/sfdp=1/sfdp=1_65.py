
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.query = torch.nn.Linear(3, 6)
        self.key   = torch.nn.Linear(3, 8)
        self.value = torch.nn.Linear(8, 10)

    def forward(self, x1):
        qk = torch.matmul(x1, self.query(x1).transpose(-2, -1))
        scale_factor = (x1.shape[1]**0.5 * torch.ones(1)) / \
                        torch.sqrt(torch.mean(torch.square(self.key(x1))))
        softmax = qk.div_(scale_factor)
        output  = torch.matmul(softmax, self.value(x1))
        return output


# Initializing the model
m = Model()

