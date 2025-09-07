This model follows the pattern above. For example:
* The input tensor is `input_tensor` with shape `(batch_size, channels, height, width)`;
* The transposed convolution output is calculated based on a mask with shape `(batch_size, channels * negative_slope, height / 2 - 1, width / 2 - 1)` (i.e., `(batch_size, 8, h/4 - 3, w/4 - 3)`);
* The where function selects elements from the input tensor or the multiplication result based on the mask;
* Then, `negative_slope` is multiplied to this result to create a new output of shape `(batch_size, channels * negative_slope, height / 2 - 1, width / 2 - 1)`.

