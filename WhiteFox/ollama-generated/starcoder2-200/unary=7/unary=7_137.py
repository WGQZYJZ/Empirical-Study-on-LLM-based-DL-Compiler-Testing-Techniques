
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear = torch.nn.Linear(512, 64)

    def forward(self, x0):
        l1 = self.linear(x0)
        l2 = l1 * F.relu(l1 + 3) / 6
        return l2


# Initializing the model and loading weights to the model from another model with different input size. 
model_a = Model()
model_b = Model().cuda() # This will change the shape of the input (from 512 to 4096).
state_dict = torch.load('./weights/pretrained-modelA-to-modelB.pth', map_location='cpu')
model_a.load_state_dict(state_dict)

 # Load model A weights into model B without changing its input shape (the number of input features will be reduced). 
 model_b.load_state_dict(model_a.state_dict())
 
 # Input to the model
x0 = torch.randn(1, 512)
 
