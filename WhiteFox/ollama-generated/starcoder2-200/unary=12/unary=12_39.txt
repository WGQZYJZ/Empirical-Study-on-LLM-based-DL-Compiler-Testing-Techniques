
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv  = torch.nn.Conv2d(3, 8, 1, stride=1, padding=0)
 
    def forward(self, x1):
        v1 = self.conv(x1) 
        v2 = torch.sigmoid(v1)
        return v1 * v2
# Initializing the model
m  = Model()

 # Inputs to the model
input_tensor = torch.randn(10,3,48,64).cuda()
 
 # Running the model and storing outputs at intermediate nodes (values of t1, t2 in this example)
intermediate_values1 = dict()
def save_layer_output(module, input, output):
    global intermediate_values1
 
    layer_name = module.__class__.__name__
    if layer_name not in  intermediate_values1.keys():
        intermediate_values1[layer_name]  = list()
     
    intermediate_values1[layer_name].append(output)

def hooker(self,input):

    print ("Hooked ",self.__class__.__name__)
    input = torch.clamp((input[0][0]), min=0.) # clip the activations
    return [input]

class Activation_clamp(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
    def forward(self, x1):
 
        return torch.clamp((x1),  min=0., max =5)
 
m = Model() # Instantiating the model

hooked_layer = m[3].register_forward_hook(hooker)


# Hooking on conv layer to find values after the conv layer in forward pass. This would return the output after Activation clamp layer. 
output = m.forward(input_tensor).cuda()

__output__  =  [list(x.data.cpu().numpy())[0][0][2] for x in intermediate_values1['Conv2d'].data.cpu()]
__expected__ = [347, 958]

