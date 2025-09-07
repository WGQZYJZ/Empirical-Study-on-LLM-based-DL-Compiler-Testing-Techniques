
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv1 = torch.nn.Conv2d(3, 8, 1, stride=1, padding=1)
        self.fc1 = torch.nn.Linear(8 * 64 * 64, 80)
        self.fc2 = torch.nn.Linear(80, 40)
 
    def forward(self, x1):
        # Step 1: Perform pointwise convolution with kernel size 1 to the input tensor
        v1 = self.conv1(x1)
        # Step 2: Scale the result of the pointwise convolution by a constant `0.5` (by dividing the output of step 1 by `2`).
        v1 *= 0.5  # Multiply the output of step 1 by 0.5
        # Step 3: Perform another pointwise convolution with kernel size 1 to the scaled result of step 2.
        v2 = self.conv1(v1)  # v2 = v1 * 0.5  # Multiply the scaled result of step 1 by 0.5
        # Step 4: Compute the error function by using `torch.erf()` on `v2` (which is already a result of step 3), and then add one to it (which will become the output of step 4).
        v3 = torch.erf(v2) + 1  # Multiply the scaled result of step 2 by the error function
        # Step 5: Scale the error function value by `0.7071067811865476` (by dividing by `sqrt(2)`), and then multiply it with `v2`, which is now a result of step 5, to compute the output of step 6.
        v4 = torch.erf(v3) / math.sqrt(2)  # Scale by sqrt(2). Multiply with the error function value from step 3 (which is already a result of step 4).
        # Step 6: Add one to the output of step 5, which will become the final result of step 6.
        v5 = v4 + 1  # The same as multiplying by `0.5`.
        # Step 7: Multiply `v2` with `v5`, and then scale it (by dividing by `sqrt(8)`), to compute the output of step 7, which is the final result of step 6.
        v6 = v2 * v5 / math.sqrt(8)  # Scale by sqrt(8). Multiply with error function value from step 5.
        return v6

# Initializing the model
m = Model()


