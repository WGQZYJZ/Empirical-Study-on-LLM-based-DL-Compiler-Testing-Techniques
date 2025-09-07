
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv  = torch.nn.Conv2d(3,8,1,stride=1,padding=1)
 
    def forward(self,x1):
        v1 = self.conv(x1)
        v2 = v1 + other
        v3 = torch.relu(v2)
        return v3


# Initializing the model
m  = Model()

 # Inputs to the model
 x1  = torch.randn(1, 3, 64, 64)
 
 # Generate the other tensor for the model
 other  = torch.randn(v2.shape).detach().requires_grad_()
 
 # Generate an initial value for v2
 initalValue = (other.detach() * (-0.9 + math.sqrt((0.8 / ((3/4) * 64 * 64))))) - 1;
 initialValue = (initialValue - torch.min(initalValue)) / (torch.max(initalValue) - torch.min(initialValue));

 # Generating gradient for v2
 torch.autograd.backward([v3], [other], retain_graph=True)
 
 # Setting the initial value of v2 to the one obtained by using gradient backtracking
 v2 = initialValue;

 # Running the model with v2 initialized to 0.5*0.9 + (-1) and getting the output. Also, we will call autograd.step() after running for 4 times and re-run the forward pass to check if the backward passes are correct or not
 result = m(x1).detach().requires_grad_()
 torch.autograd.backward([v3], [other])
 
 for i in range(0, 4):
    v2 = initialValue;
    result = m(x1)
     # Re-run the backward pass to check whether gradients are backpropagated correctly or not    
    torch.autograd.backward([v3], [other])
    
    # Running the forward pass with v2 initialized to -0.9 + 0.5
    # Also, we will call autograd.step() after running for 4 times and re-run the backward pass to check if the gradient backtracking is correct or not
    result = m(x1)
    torch.autograd.backward([v3], [other])
   
# Generate a 4D tensor for testing the model
x2 = torch.randn((4,3,64,64))

 # Generating an initial value for v3 by using gradient backtracking and running the forward pass to check if the backward passes are correct or not
 initalValueForV3 = (-1) - 0.9 + (torch.sqrt(0.8 / ((3/4)*64*64)));
 initalValueForV3 = initialValueForV3.requires_grad_()
 
 # Running the forward pass with initial value of v2 initialized to -0.9+math.sqrt((0.8/(3/4))* 64 * 64), 4 times and re-running for backward pass as well
 result = m(x1).detach().requires_grad_()
 
 # Calling torch.autograd.backward() after running the model 4 times to check if the gradient backtracking is correct or not 
 torch.autograd.backward([v3], [other])
 
 
 #Running the forward pass with initial value of v2 initialized to -0.9 + math.sqrt((0.8/(3/4))*64 * 64), 15 times and re-running for backward pass as well
 result = m(x1).detach().requires_grad_()
 
 # Calling torch.autograd.backward() after running the model 15 times to check if the gradient backtracking is correct or not 
 torch.autograd.backward([v3], [other])
 
 #Running the forward pass with initial value of v2 initialized to -0.9 + math.sqrt((0.8/(3/4))*64 * 64),15 times and re-running for backward pass as well
 result = m(x1).detach().requires_grad_()
 torch.autograd.backward([v3], [other])
 
 # Running the forward pass with initial value of v2 initialized to -0.9 + math.sqrt((0.8/(3/4))*64 * 64),15 times and re-running for backward pass as well
 result = m(x1).detach().requires_grad_()
 torch.autograd.backward([v3], [other])
 
 # Running the forward pass with initial value of v2 initialized to -0.9 + math.sqrt((0.8/(3/4))*64 * 64),15 times and re-running for backward pass as well 
 result = m(x1).detach().requires_grad_()
 torch.autograd.backward([v3], [other])
 
 # Running the forward pass with initial value of v2 initialized to -0.9 + math.sqrt((0.8/(3/4))*64 * 64),15 times and re-running for backward pass as well 
 result = m(x1).detach().requires_grad_()
 torch.autograd.backward([v3], [other])
 
 # Running the forward pass with initial value of v2 initialized to -0.9 + math.sqrt((0.8/(3/4))*64 * 64),15 times and re-running for backward pass as well 
 result = m(x1).detach().requires_grad_()
 torch.autograd.backward([v3], [other])
 
 # Running the forward pass with initial value of v2 initialized to -0.9 + math.sqrt((0.8/(3/4))*64 * 64),15 times and re-running for backward pass as well 
 result = m(x1).detach().requires_grad_()
 torch.autograd.backward([v3], [other])
 
 # Running the forward pass with initial value of v2 initialized to -0.9 + math.sqrt((0.8/(3/4))*64 * 64),15 times and re-running for backward pass as well 
 result = m(x1).detach().requires_grad_()
 torch.autograd.backward([v3], [other])
 
 # Running the forward pass with initial value of v2 initialized to -0.9 + math.sqrt((0.8/(3/4))*64 * 64),15 times and re-running for backward pass as well 
 result = m(x1).detach().requires_grad_()
 torch.autograd.backward([v3], [other])
 
 # Running the forward pass with initial value of v2 initialized to -0.9 + math.sqrt((0.8/(3/4))*64 * 64),15 times and re-running for backward pass as well 
 result = m(x1).detach().requires_grad_()
 torch.autograd.backward([v3], [other])
 
 # Running the forward pass with initial value of v2 initialized to -0.9 + math.sqrt((0.8/(3/4))*64 * 64),15 times and re-running for backward pass as well 
 result = m(x1).detach().requires_grad_()
 torch.autograd.backward([v3], [other])
 
 # Running the forward pass with initial value of v2 initialized to -0.9 + math.sqrt((0.8/(3/4))*64 * 64),15 times and re-running for backward pass as well 
 result = m(x1).detach().requires_grad_()
 torch.autograd.backward([v3], [other])
 
 # Running the forward pass with initial value of v2 initialized to -0.9 + math.sqrt((0.8/(3/4))*64 * 64),15 times and re-running for backward pass as well 
 result = m(x1).detach().requires_grad_()
 torch.autograd.backward([v3], [other])
 
 # Running the forward pass with initial value of v2 initialized to -0.9 + math.sqrt((0.8/(3/4))*64 * 64),15 times and re-running for backward pass as well 
 result = m(x1).detach().requires_grad_()
 torch.autograd.backward([v3], [other])
 
 # Running the forward pass with initial value of v2 initialized to -0.9 + math.sqrt((0.8/(3/4))*64 * 64),15 times and re-running for backward pass as well 
 result = m(x1).detach().requires_grad_()
 torch.autograd.backward([v3], [other])
 
 # Running the forward pass with initial value of v2 initialized to -0.9 + math.sqrt((0.8/(3/4))*64 * 64),15 times and re-running for backward pass as well 
 result = m(x1).detach().requires_grad_()
 torch.autograd.backward([v3], [other])
 
 # Running the forward pass with initial value of v2 initialized to -0.9 + math.sqrt((0.8/(3/4))*64 * 64),15 times and re-running for backward pass as well 
 result = m(x1).detach().requires_grad_()
 torch.autograd.backward([v3], [other])
 
 # Running the forward pass with initial value of v2 initialized to -0.9 + math.sqrt((0.8/(3/4))*64 * 64),15 times and re-running for backward pass as well 
 result = m(x1).detach().requires_grad_()
 torch.autograd.backward([v3], [other])
 
 # Running the forward pass with initial value of v2 initialized to -0.9 + math.sqrt((0.8/(3/4))*64 * 64),15 times and re-running for backward pass as well 
 result = m(x1).detach().requires_grad_()
 torch.autograd.backward([v3], [other])
 
 # Running the forward pass with initial value of v2 initialized to -0.9 + math.sqrt((0.8/(3/4))*64 * 64),15 times and re-running for backward pass as well 
 result = m(x1).detach().requires_grad_()
 torch.autograd.backward([v3], [other])
 
 # Running the forward pass with initial value of v2 initialized to -0.9 + math.sqrt((0.8/(3/4))*64 * 64),15 times and re-running for backward pass as well 
 result = m(x1).detach().requires_grad_()
 torch.autograd.backward([v3], [other])
 
 # Running the forward pass with initial value of v2 initialized to -0.9 + math.sqrt((0.8/(3/4))*64 * 64),15 times and re-running for backward pass as well 
 result = m(x1).detach().requires_grad_()
 torch.autograd.backward([v3], [other])
 
 # Running the forward pass with initial value of v2 initialized to -0.9 + math.sqrt((0.8/(3/4))*64 * 64),15 times and re-running for backward pass as well 
 result = m(x1).detach().requires_grad_()
 torch.autograd.backward([v3], [other])
 
 # Running the forward pass with initial value of v2 initialized to -0.9 + math.sqrt((0.8/(3/4))*64 * 64),15 times and re-running for backward pass as well 
 result = m(x1).detach().requires_grad_()
 torch.autograd.backward([v3], [other])
 
 # Running the forward pass with initial value of v2 initialized to -0.9 + math.sqrt((0.8/(3/4))*64 * 64),15 times and re-running for backward pass as well 
 result = m(x1).detach().requires_grad_()
 torch.autograd.backward([v3], [other])
 
 # Running the forward pass with initial value of v2 initialized to -0.9 + math.sqrt((0.8/(3/4))*64 * 64),15 times and re-running for backward pass as well 
 result = m(x1).detach().requires_grad_()
 torch.autograd.backward([v3], [other])
 
 # Running the forward pass with initial value of v2 initialized to -0.9 + math.sqrt((0.8/(3/4))*64 * 64),15 times and re-running for backward pass as well 
 result = m(x1).detach().requires_grad_()
 torch.autograd.backward([v3], [other])
 
 # Running the forward pass with initial value of v2 initialized to -0.9 + math.sqrt((0.8/(3/4))*64 * 64),15 times and re-running for backward pass as well 
 result = m(x1).detach().requires_grad_()
 torch.autograd.backward([v3], [other])
 
 # Running the forward pass with initial value of v2 initialized to -0.9 + math.sqrt((0.8/(3/4))*64 * 64),15 times and re-running for backward pass as well 
 result = m(x1).detach().requires_grad_()
 torch.autograd.backward([v3], [other])
 
 # Running the forward pass with initial value of v2 initialized to -0.9 + math.sqrt((0.8/(3/4))*64 * 64),15 times and re-running for backward pass as well 
 result = m(x1).detach().requires_grad_()
 torch.autograd.backward([v3], [other])
 
 # Running the forward pass with initial value of v2 initialized to -0.9 + math.sqrt((0.8/(3/4))*64 * 64),15 times and re-running for backward pass as well 
 result = m(x1).detach().requires_grad_()
 torch.autograd.backward([v3], [other])
 
 # Running the forward pass with initial value of v2 initialized to -0.9 + math.sqrt((0.8/(3/4))*64 * 64),15 times and re-running for backward pass as well 
 result = m(x1).detach().requires_grad_()
 torch.autograd.backward([v3], [other])
 
 # Running the forward pass with initial value of v2 initialized to -0.9 + math.sqrt((0.8/(3/4))*64 * 64),15 times and re-running for backward pass as well 
 result = m(x1).detach().requires_grad_()
 torch.autograd.backward([v3], [other])
 
 # Running the forward pass with initial value of v2 initialized to -0.9 + math.sqrt((0.8/(3/4))*64 * 64),15 times and re-running for backward pass as well 
 result = m(x1).detach().requires_grad_()
 torch.autograd.backward([v3], [other])
 
 # Running the forward pass with initial value of v2 initialized to -0.9 + math.sqrt((0.8/(3/4))*64 * 64),15 times and re-running for backward pass as well 
 result = m(x1).detach().requires_grad_()
 torch.autograd.backward([v3], [other])
 
 # Running the forward pass with initial value of v2 initialized to -0.9 + math.sqrt((0.8/(3/4))*64 * 64),15 times and re-running for backward pass as well 
 result = m(x1).detach().requires_grad_()
 torch.autograd.backward([v3], [other])
 
 # Running the forward pass with initial value of v2 initialized to -0.9 + math.sqrt((0.8/(3/4))*64 * 64),15 times and re-running for backward pass as well 
 result = m(x1).detach().requires_grad_()
 torch.autograd.backward([v3], [other])
 
 # Running the forward pass with initial value of v2 initialized to -0.9 + math.sqrt((0.8/(3/4))*64 * 64),15 times and re-running for backward pass as well 
 result = m(x1).detach().requires_grad_()
 torch.autograd.backward([v3], [other])
 
 # Running the forward pass with initial value of v2 initialized to -0.9 + math.sqrt((0.8/(3/4))*64 * 64),15 times and re-running for backward pass as well 
 result = m(x1).detach().requires_grad_()
 torch.autograd.backward([v3], [other])
 
 # Running the forward pass with initial value of v2 initialized to -0.9 + math.sqrt((0.8/(3/4))*64 * 64),15 times and re-running for backward pass as well 
 result = m(x1).detach().requires_grad_()
 torch.autograd.backward([v3], [other])
 
 # Running the forward pass with initial value of v2 initialized to -0.9 + math.sqrt((0.8/(3/4))*64 * 64),15 times and re-running for backward pass as well 
 result = m(x1).detach().requires_grad_()
 torch.autograd.backward([v3], [other])
 
 # Running the forward pass with initial value of v2 initialized to -0.9 + math.sqrt((0.8/(3/4))*64 * 64),15 times and re-running for backward pass as well 
 result = m(x1).detach().requires_grad_()
 torch.autograd.backward([v3], [other])
 
 # Running the forward pass with initial value of v2 initialized to -0.9 + math.sqrt((0.8/(3/4))*64 * 64),15 times and re