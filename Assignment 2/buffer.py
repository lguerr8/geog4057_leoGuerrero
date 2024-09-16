import arcpy
arcpy.analysis.Buffer(
    in_features="cities.shp",
    out_feature_class="./cities_buffer_1.shp",
    buffer_distance_or_field="100 Meters",
    line_side="FULL",
    line_end_type="ROUND",
    dissolve_option="NONE",
    dissolve_field=None,
    method="PLANAR"
)