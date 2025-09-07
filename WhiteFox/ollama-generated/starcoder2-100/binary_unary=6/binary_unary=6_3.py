
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear = torch.nn.Linear(30, 128)
 
    def forward(self, x1):
        v1 = self.linear(x1)
        v2 = v1 - other 
        v3 = torch.relu(v2)
        return v3


# Initializing the model and assigning 'other' to a random number from [-5., 0.]
m  = Model()
random_num = torch.rand(()).sub_(0.5).mul_(10.).add(5.)
other = random_num[0]

 # Inputs to the model 
 x1  = torch.randn(32, 30)
 
  # Initializing the module using Pytorch native APIs
 torch.nn.Linear(30, 128).to_sparse()
 
 # Initializing the module using pytorch_model_inspector native APIs that automatically detects input tensors, forward function, and initializations for various models
 inputs = m._get_input_shapes(x1)
 x1, forward_, initalizations = inputs.values()[0]

 # Generating an adversarial example by changing the values of certain inputs/weights to produce an adversarial output
 adversary = m._generate_adversarial(initalizations, forward_, other=other)

 # Run the adversarial example 
 adv_output  = m(*x1)
 
