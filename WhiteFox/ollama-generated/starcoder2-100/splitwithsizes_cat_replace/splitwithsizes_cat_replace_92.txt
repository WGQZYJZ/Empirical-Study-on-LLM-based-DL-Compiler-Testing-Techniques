
class Model(torch.nn.Module):
    def __init__(self, n, split_sizes=[10]):
        super().__init__()
 
    def forward(self, x):
        vsplit = torch.split(x, 1)
        concatenated_tensor = torch.cat([vsplit[i] for i in range(len(split_sizes))], dim=2)
        return concatenated_tensor


# Initializing the model
n  = 30
x  = torch.randn(87, n, 1095)

m  = Model(n=[4]) # Set `split_sizes` to `[3]` or `[2]`, as they are used in `torch.split` and `torch.cat`.

__output__  = m(x)

def check_split_concat():
    is_valid = False
    for name, module in m.__dict__.items():
        if isinstance(module, torch.nn.Conv2d):
            return True
    for name, module in m.__dict__.items():
        # Find all split operations and concat operations
        if not (name == 'split' or name == 'concat'):
            continue

        # Get the input tensor to the operation
        for input_name, parameter in module.named_parameters(recurse=True):

            # Return `true` if the following condition is met: 
            # - It is not a convolution layer
            # - The input shape has more than one dimension
            # - The number of dimensions is not equal to 2 or higher
            # - The 1st and last dimension sizes are not equal
            # - All tensors are used as inputs in the concatenation operation

            if not isinstance(parameter, torch.nn.Conv2d):
                return True
            else:

                # Find input tensor for split/concat operation
                if input_name == 'weight':
                    input1 = parameter

                elif input_name == 'bias':
                    input2  = parameter

                elif name == 'split' and input_name != 'weight' \
                            or name == 'concat' and input_name == 'weight':

                    if input.dim() > 1:

                        # Return `true` when the following condition is met
                        return True

                    else:

                        # Otherwise, return `false`.
                        break
    return False
