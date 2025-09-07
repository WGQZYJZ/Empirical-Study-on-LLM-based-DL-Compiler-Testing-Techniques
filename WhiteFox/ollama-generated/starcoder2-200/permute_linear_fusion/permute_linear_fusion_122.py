
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear  = torch.nn.Linear(2, 2)

    def forward(self, x1):
        v1  = x1.permute(0, 3, 1, 2).reshape(-1, 2 * 4) # Swapping the 4th and 5th dimensions of an input tensor, then reshaping it to a 6D tensor. 
        v2 = torch.nn.functional.linear(v1, self.linear.weight, self.linear.bias)
        return v2

# Initializing the model
m  = Model()

