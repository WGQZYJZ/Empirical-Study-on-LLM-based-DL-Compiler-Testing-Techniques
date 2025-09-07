
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.input  = torch.randn(10, 3) # The input tensor
        self.mat1  = torch.randn(5, 784) * .23 + torch.tensor(69.) 
        self.mat2  = torch.randn(10, 784) * -0.33 + 1.7
 
        dim  = random_choice(range(-len(input), len(input)))
        self.t2  = torch.cat([torch.addmm(self.input, self.mat1, self.mat2)], dim=dim)
 
 # Initializing the model
 m  = Model()

 # Inputs to the model
 x1  = np.random.choice(range(-m.input.shape[0], m.input.shape[0])) 
 __output__  = m(x1)

