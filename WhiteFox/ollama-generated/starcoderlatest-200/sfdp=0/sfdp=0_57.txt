
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
        self.query = torch.nn.Conv2d(3, 8, 1, stride=1, padding=1)
        self.key = torch.nn.Conv2d(3, 8, 1, stride=1, padding=1)
 
    def forward(self, x1):
        scaled_dot_product = torch.matmul(
            self.query(x1), 
            self.key(x1).transpose(-2, -1) 
        ) / math.sqrt(float(64))
 
        attention_weights = scaled_dot_product.softmax(dim=-1)
        output = attention_weights.matmul(self.value(x1))
        return output
 
    def __setattr__(self, attr, value):
        if "value" in self.__dict__:
            print("Updating attribute `{}`...".format(attr))
        super().__setattr__(attr, value)
 

# Initializing the model
m = Model()


# Inputs to the model
x1 = torch.randn(1, 3, 64, 64)
