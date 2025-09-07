
class Model(torch.nn.Module):
    def __init__(self, input1=30, output2 =50):
        super().__init__()

        self.l1 = torch.nn.Linear(input1 ,output2)
    
    def forward(self, input):
        l1  = self.l1(input)
        l2  = l1 * clamp(min=0, max=6, l1 + 3)# multiply the output of linear by the clamped output of the multiplication added with three
        l3  = l2 / 6# divide the output of the multiplication by six
        return l3


# Initializing the model
model = Model(input_1)

# Input to the model: 
input = torch.ones((50,))

