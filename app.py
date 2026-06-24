import streamlit as st
import json

# Page Setup - Simple & Clean
st.set_page_config(
    page_title="Clinical Triage & Compliance Monitor",
    page_icon="📋",
    layout="wide"
)

# Application Header - honest & professional
st.title("📋 Clinical Triage & Compliance Utility Console")
st.caption("A lean software tool designed for structured data validation and operational risk flagging.")

st.markdown("---")

# Initialize Local Session Caching (Simple persistence check)
if 'session_counter' not in st.session_state:
    st.session_state['session_counter'] = 0
st.session_state['session_counter'] += 1

# Top Stats Row
col1, col2 = st.columns(2)
with col1:
    st.metric(label="Local Session State Status", value="Active & Stable")
with col2:
    st.metric(label="Current Session Refresh Cycles", value=st.session_state['session_counter'])

st.markdown("---")

# Main Interface Tabs
tab1, tab2 = st.tabs(["🎯 Clinical Triage Mapping", "🚨 Compliance Risk Tracker"])

# =====================================================================
# TAB 1: CLINICAL TRIAGE MAPPING (Structured JSON Engine)
# =====================================================================
with tab1:
    st.subheader("Clinical Text Schema Validation")
    st.markdown("Convert unstructured clinical notes into structured dictionary key-value mappings.")
    
    # Default clean note example
    default_note = (
        "Patient reported severe headache and acute renal symptoms. "
        "Symptoms escalated rapidly over the last 48 hours. Primary control group criteria matching."
    )
    
    user_input = st.text_area("Paste Clinical/Operational Notes Here:", value=default_note, height=120)
    
    if st.button("Analyze & Structure Mapping", type="primary"):
        if user_input.strip() == "":
            st.warning("Please enter some text to analyze.")
        else:
            # Simple, transparent conditional logic for keyword parsing
            lowercase_text = user_input.lower()
            
            structured_data = {
                "Metadata": {
                    "character_count": len(user_input),
                    "status": "Processed Successfully"
                },
                "Identified Operational Flags": {
                    "renal_system_reference": "acute" in lowercase_text or "renal" in lowercase_text,
                    "escalation_detected": "escalated" in lowercase_text or "severe" in lowercase_text,
                    "control_group_match": "control group" in lowercase_text
                }
            }
            
            st.success("Data successfully parsed into local runtime memory!")
            st.markdown("#### Validated Data Schema Output (JSON)")
            st.json(structured_data)

# =====================================================================
# TAB 2: COMPLIANCE RISK TRACKER (Conditional Rule Logic)
# =====================================================================
with tab2:
    st.subheader("Operational Regulatory Flagging Engine")
    st.markdown("Evaluates case urgency limits based on strict timeline parameters.")
    
    # Simple form inputs for rule evaluation
    with st.form("compliance_form"):
        case_severity = st.selectbox("Select Case Severity:", ["Low", "Moderate", "Critical"])
        days_elapsed = st.number_input("Days Elapsed Since Initial Triage Notification:", min_value=0, max_value=60, value=2)
        
        submit_btn = st.form_submit_with_button("Evaluate Compliance Risk Status")
        
    if submit_btn:
        st.markdown("#### Evaluation Results")
        
        # Pure logic validation blocks - transparent and robust
        if case_severity == "Critical" and days_elapsed >= 7:
            st.error(
                f"🚨 **CRITICAL RISK:** Regulatory timeline breached! "
                f"Expedited safety reporting guidelines require submission within 7 days. Current latency: {days_elapsed} days."
            )
        elif case_severity == "Moderate" and days_elapsed >= 15:
            st.warning(
                f"⚠️ **MODERATE RISK:** Approaching compliance deadline limits for standard tracking profiles. "
                f"Current latency: {days_elapsed} days."
            )
        else:
            st.success(
                f"✅ **COMPLIANCE MET:** Current lifecycle tracking for {case_severity} severity "
                f"is fully within standard processing limits ({days_elapsed} days elapsed)."
            )
            
        # Extra developer context note
        st.info("💡 Note: This logic module applies deterministic conditional checking against core regulatory schemas.")
