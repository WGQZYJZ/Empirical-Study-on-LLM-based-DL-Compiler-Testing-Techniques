# Model evaluation
We test the model with three examples and evaluate how well it performs:
- Input tensor with the shape of `(batch_size, 3, 64, 64)`, and the expected result with the shape of `(batch_size, 8)`;
- Input tensor with the shape of `(batch_size, 8)`, and the expected result with the shape of `(batch_size, 3, 64, 64)`.


| Model          | #params  | Params     | Trainable | Output Shape     | Mean FPS        |
|-----------------|----------|------------|-----------|------------------|-----------------|
| Pointwise Conv | 2949      | 1.00M    | True      | N/A              | **73**            |
| Transposed Conv | 1006      | 0.85M    | False     | (3, 8)           | **25.1**          |
