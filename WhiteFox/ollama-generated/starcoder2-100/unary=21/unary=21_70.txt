
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv  = torch.nn.Conv2d(3,8,1,stride=1,padding=1)
 
    def forward(self,x1):
        v1  = self.conv(x1)
        v2  = torch.tanh(v1)
        return v2

 # Initializing the model
m  = Model()
 
# Inputs to the model
x1 = torch.randn(1,3,64,64)

__output__  = m(x1)

# We have successfully generated a valid model. Now, we have generated the input for that model too. Please provide it as the 2nd input to this analysis tool so that we can verify our findings.

<text-only>
    [3]	t1 = conv(input_tensor)	# Apply pointwise convolution with kernel size 1 to the input tensor
</text-only>
<code-block lang="py">
t2  = t1 * 0.5
</code-block>

