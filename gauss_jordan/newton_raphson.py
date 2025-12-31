def f(x, y):
    # The function we want to minimize: f(x, y) = x^2 + y^2
    return x**2 + y**2

def get_gradient(x, y, h=1e-5):
    # Manual partial derivatives
    df_dx = (f(x + h, y) - f(x - h, y)) / (2 * h)
    df_dy = (f(x, y + h) - f(x, y - h)) / (2 * h)
    return [df_dx, df_dy]

def get_hessian(x, y, h=1e-4):
    # Manual second-order partial derivatives
    f_xx = (f(x + h, y) - 2 * f(x, y) + f(x - h, y)) / (h**2)
    f_yy = (f(x, y + h) - 2 * f(x, y) + f(x, y - h)) / (h**2)
    
    # Mixed partial derivative (f_xy)
    f_xy = (f(x+h, y+h) - f(x+h, y-h) - f(x-h, y+h) + f(x-h, y-h)) / (4 * h**2)
    
    return [[f_xx, f_xy], 
            [f_xy, f_yy]]

def solve_newton_step(curr_x, curr_y):
    grad = get_gradient(curr_x, curr_y)
    hess = get_hessian(curr_x, curr_y)
    
    # To find the "correct path" step (delta), we solve: Hessian * delta = -Gradient
    # For a 2x2 matrix [[a, b], [c, d]], the inverse is (1/det) * [[d, -b], [-c, a]]
    det = hess[0][0] * hess[1][1] - hess[0][1] * hess[1][0]
    
    if abs(det) < 1e-9: return 0, 0 # Avoid division by zero
    
    inv_hess = [[hess[1][1]/det, -hess[0][1]/det],
                [-hess[1][0]/det, hess[0][0]/det]]
    
    # delta = -inv_hess * grad
    step_x = -(inv_hess[0][0] * grad[0] + inv_hess[0][1] * grad[1])
    step_y = -(inv_hess[1][0] * grad[0] + inv_hess[1][1] * grad[1])
    
    return step_x, step_y

# Optimization loop
x, y = 10.0, 10.0 # Starting point
for i in range(5):
    dx, dy = solve_newton_step(x, y)
    x += dx
    y += dy
    print(f"Step {i+1}: x={x:.4f}, y={y:.4f}")