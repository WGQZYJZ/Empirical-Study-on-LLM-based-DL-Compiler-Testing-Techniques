

class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear = torch.nn.Linear(1, 2)
 
    def forward(self, x1):
        v1 = self.linear(x1)
        v2 = v1 * 0.5
        v3 = v1 * 0.7071067811865476
        v4 = torch.erf(v3)
        v5 = v4 + 1
        v6 = v2 * v5
        return v6

# Initializing the model
m = Model()


# Inputs to the model
x1 = torch.randn(1, 1).view(-1, 1)

# Expected output: 3.074984e-02
__output__  = m(x1)

# Evaluation (This section must be present in all examples.)
import os
os.environ['TOKENIZERS_PARALLELISM'] = 'false' # Ensure determinism when tokenizing with Tokenizers.
from traintk import check, get_metric
__output__, metric, config = check(model_input=x1, metric_name='mean_absolute')
print(__output__, metric)