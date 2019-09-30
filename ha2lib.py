def imply(lhs,rhs):
    return((not lhs) or rhs)

# student sat'd course prereq's with B or better

def studentGotAorB(ssn, dcode, cno, transcript):
    aOrB = "tbd"
    return(aOrB)

def studentSatCoursePrereqs(ssn,dcode,cno,univDB):

    prereqsSatisfied = "tbd"
    return(prereqsSatisfied)

def studentSatClassPrereqs(ssn,cl,univDB):
    prereqsSatisfied = "tbd"
    return(prereqsSatisfied)

def ha2(univDB):
    tables = univDB["tables"]
    department = tables["department"]
    course = tables["course"]
    prereq = tables["prereq"]
    class_ = tables["class"]
    faculty = tables["faculty"]
    student = tables["student"]
    enrollment = tables["enrollment"]
    transcript = tables["transcript"]

# boolean queries
    boolQuery_a = "tbd"
    boolQuery_b = "tbd"
    boolQuery_c = "tbd"
    boolQuery_d = "tbd"
    boolQuery_e = "tbd"
    boolQuery_f = "tbd"
    boolQuery_g = "tbd"
    boolQuery_i = "tbd"
    boolQuery_h = "tbd"
    boolQuery_i = "tbd"
    boolQuery_j = "tbd"
    boolQuery_k = "tbd"
    boolQuery_l = "tbd"
    dataQuery_a = "tbd"
    dataQuery_b = "tbd"
    dataQuery_c = "tbd"
    dataQuery_d = "tbd"
    dataQuery_e = "tbd"
    dataQuery_f = "tbd"
    dataQuery_g = "tbd"
    dataQuery_h = "tbd"
    dataQuery_i = "tbd"
    dataQuery_j = "tbd"
    return({
        "boolQuery_a": boolQuery_a,
        "boolQuery_b": boolQuery_b,
        "boolQuery_c": boolQuery_c,
        "boolQuery_d": boolQuery_d,
        "boolQuery_e": boolQuery_e,
        "boolQuery_f": boolQuery_f,
        "boolQuery_g": boolQuery_g,
        "boolQuery_h": boolQuery_h,
        "boolQuery_i": boolQuery_i,
        "boolQuery_j": boolQuery_j,
        "boolQuery_k": boolQuery_k,
        "boolQuery_l": boolQuery_l,
        "dataQuery_a": dataQuery_a,
        "dataQuery_b": dataQuery_b,
        "dataQuery_c": dataQuery_c,
        "dataQuery_d": dataQuery_d,
        "dataQuery_e": dataQuery_e,
        "dataQuery_f": dataQuery_f,
        "dataQuery_g": dataQuery_g,
        "dataQuery_h": dataQuery_h,
        "dataQuery_i": dataQuery_i,
        "dataQuery_j": dataQuery_j
    })
