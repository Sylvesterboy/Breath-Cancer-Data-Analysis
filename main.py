from pydantic import BaseModel
class cancer_class(BaseModel):
    mean_radius : float
    mean_perimeter : float
    mean_area : float
    mean_compactness : float
    mean_concavity : float
    mean_concave_points : float
    radius_error : float
    perimeter_error : float
    area_error : float
    worst_radius : float
    worst_perimeter : float
    worst_area : float
    worst_compactness : float
    worst_concavity : float
    worst_concave_points : float