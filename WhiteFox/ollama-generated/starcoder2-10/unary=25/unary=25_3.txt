

class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear  = torch.nn.Linear(32, 64)

    def forward(self, x1):
        v0 = self.linear(x1) # Applying a linear transformation to the input tensor

        b = (v0 > 0).detach() # Creating a boolean tensor where each element is True if the corresponding element in t1 is greater than 0, and False otherwise

        n = x1 * negative_slope
        v1 = torch.where(b, v0, n) # For each element in b, if the element is True, choose the corresponding element from t2, otherwise choose the corresponding element from n


        return v1

m  = Model()


x1  = torch.randn(32, 64)

__output__  = m(x1)


