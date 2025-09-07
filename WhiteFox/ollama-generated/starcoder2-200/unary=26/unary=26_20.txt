
class Model(torch.nn.Module):
    def __init__(self, negative_slope = 0.25) -> None:
        super().__init__()

        self.convTranspose = torch.nn.ConvTranspose2d(8, 3, kernelSize=1, stride=1, padding=0)
        self.negativeSlope = negative_slope
 
    def forward(self, inputTensor):
        v1 = self.convTranspose(inputTensor) # Apply pointwise transposed convolution to the input tensor 
        v2 = v1 > 0;                         # Create a mask where each element is True if the corresponding element in v1 is greater than 0, False otherwise
        v3 = torch.where(v2, v1, self.negativeSlope*v1) # Apply the where function to select elements from v1 or v3 based on the mask v2
        return v3

# Initializing the model
model = Model()


Inputs to the model
x  = torch.randn(1,8,64,64); # The input tensor is randomly generated with shape (1, 8, 64, 64)


__output__= m(x)

The output of the convolution should be a tensor with the following shape: (batch_size, 3, H, W) or (N, Cin, 1), where N is an integer >=0 and the value 0 represents undetermined. The batch size in the output can also depend on the input sizes. The output of the Leaky ReLU should be the same shape as that of the original transposed convolution.

The output of the pointwise transposed convolution is a tensor with the following shape: (N, Cout, H, W) or (N, 1), where N and Cout are determined, while Cin in the output can depend on other parameters. The shape (1,) represents undetermined dimensions.

The output of the mask should be a tensor with the same shape as that of the input: (batch_size, 32).

# Scoring
Your model will receive a score. It will be scaled linearly and capped between 0 to 10 points, depending on the completeness of your PyTorch model. You also need to submit:
  - The inputs/outputs of the generated model (model.forward(input)). In particular, it should include the input tensor in the form of model_inputs. You can define a function that generates the inputs before submission using this format: `def get_input() -> torch.Tensor:` . Note: you should include the type for model_inputs argument as torch.Tensor as it will be automatically re-instantiated as torch.Tensor:

def get_input():
    return torch.randn(1, 32)

The final score will be divided by the length of the input. For instance, you have 8 models. Your model scores should be [7 points, 5 points, 9 points]. The total points are 34 (which corresponds to an average of 8.5 points for each model).

