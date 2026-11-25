# -*- coding: utf-8 -*-
import os

part1 = r"""'use client';

import React, { useState, useEffect, useRef } from 'react';
import Link from 'next/link';
import { useRouter } from 'next/navigation';
import {
  Shield,
  ArrowRight,
  GitFork,
  Cpu,
  Layers,
  CheckCircle2,
  AlertTriangle,
  Play,
  Zap,
  Lock,
  Menu,
  X,
  ChevronRight,
  ChevronDown,
  FileCheck2,
  Search,
  Network,
  Box,
  RefreshCw,
  BarChart3,
  Radar,
  Server,
  Terminal,
  Activity,
  Workflow,
  Clock,
  AlertOctagon,
  Database,
  Key,
  ShieldCheck,
  Eye,
  SlidersHorizontal,
  FileText,
  RotateCcw,
  Sparkles,
  ArrowUpRight,
  Check,
  Code2,
  Gauge,
  Radio,
  Sliders,
  Send,
  Linkedin,
  Twitter,
  Youtube,
  Github,
} from 'lucide-react';
import { useAuth } from '@/lib/auth-context';
import { api } from '@/lib/api';
import CyberCanvas, { CANONICAL_NODES } from '@/components/CyberCanvas';

/* ═══════════════════════════════════════════════════════════════════════
   1. BRAND ASSETS & LOGOS
   ═══════════════════════════════════════════════════════════════════════ */

function RakshasetuShield({ className = 'w-6 h-6' }: { className?: string }) {
  return (
    <svg viewBox="0 0 32 36" fill="none" xmlns="http://www.w3.org/2000/svg" className={className}>
      <path
        d="M16 2L3 6.5V17C3 25 8.5 31.5 16 34C23.5 31.5 29 25 29 17V6.5L16 2Z"
        stroke="#C68E6D"
        strokeWidth="2"
        strokeLinejoin="round"
        fill="#11141B"
      />
      <path d="M10 13V24M22 13V24" stroke="#E8E3DB" strokeWidth="1.5" strokeLinecap="round" />
      <path
        d="M6 18C10 15 14 15 16 17C18 15 22 15 26 18"
        stroke="#C68E6D"
        strokeWidth="1.5"
        strokeLinecap="round"
      />
      <path d="M10 20H22" stroke="#C68E6D" strokeWidth="1.2" strokeLinecap="round" />
      <circle cx="16" cy="11" r="1.5" fill="#D7A384" />
    </svg>
  );
}

function NvidiaLogo({ className = 'w-4 h-4' }: { className?: string }) {
  return (
    <svg viewBox="0 0 24 24" fill="currentColor" className={className}>
      <path d="M8.948 6.257c-1.465 0-2.822.42-3.957 1.134a9.712 9.712 0 0 0-4.991 8.544c0 3.791 2.222 7.086 5.467 8.652-.164-.727-.254-1.474-.254-2.228 0-4.045 2.508-7.551 6.183-8.824-1.439-.816-2.448-2.34-2.448-4.095 0-1.745.998-3.26 2.426-4.081-.884-.336-1.848-.521-2.854-.521L8.948 6.257zm7.643 1.092c-2.47 0-4.484 2.015-4.484 4.484 0 2.47 2.014 4.484 4.484 4.484 2.47 0 4.484-2.014 4.484-4.484 0-2.469-2.014-4.484-4.484-4.484zm-7.643 4.484c0 1.258.536 2.404 1.401 3.208-1.579.882-2.651 2.56-2.651 4.488 0 .548.094 1.077.256 1.579C6.01 19.865 4.773 17.65 4.773 15.08c0-3.32 2.083-6.177 5.06-7.34-.564.811-.885 1.785-.885 2.827v.266zm10.74 3.738a9.696 9.696 0 0 0 4.312-8.109c0-5.385-4.366-9.752-9.752-9.752-2.31 0-4.437.808-6.117 2.164 1.157-.735 2.535-1.164 4.01-1.164 3.992 0 7.243 3.25 7.243 7.243 0 2.378-1.15 4.498-2.929 5.834 1.442.81 2.518 2.215 2.873 3.904l.36-.12z" />
    </svg>
  );
}

/* ═══════════════════════════════════════════════════════════════════════
   2. GLOWING SECTION DIVIDER WITH ORBITAL FLARE
   ═══════════════════════════════════════════════════════════════════════ */

function GlowingSectionDivider() {
  return (
    <div className="relative w-full py-6 pointer-events-none overflow-hidden flex items-center justify-center">
      {/* Horizontal laser track */}
      <div className="absolute inset-x-0 h-px bg-gradient-to-r from-transparent via-[#C68E6D]/40 to-transparent" />
      {/* Left flare burst */}
      <div className="absolute -left-12 w-48 h-12 bg-gradient-to-r from-[#C68E6D]/25 to-transparent blur-xl" />
      {/* Right flare burst */}
      <div className="absolute -right-12 w-48 h-12 bg-gradient-to-l from-[#C68E6D]/25 to-transparent blur-xl" />
      {/* Center glowing bead */}
      <div className="w-32 h-0.5 rounded-full bg-gradient-to-r from-transparent via-[#E8E3DB] to-transparent shadow-[0_0_16px_#C68E6D]" />
    </div>
  );
}

/* ═══════════════════════════════════════════════════════════════════════
   3. DATA TYPES & CANONICAL DEFINITIONS
   ═══════════════════════════════════════════════════════════════════════ */

interface FailureMode {
  id: string;
  badge: string;
  title: string;
  sourceNode: string;
  affectedServices: string[];
  disruptionLevel: 'High' | 'Critical' | 'Medium';
  tagColor: string;
  narrative: string;
  rootCause: string;
}

const FAILURE_MODES: FailureMode[] = [
  {
    id: 'policy_drift',
    badge: 'XACML / ABAC Policy Engine',
    title: 'Conditional Access Policy Drift',
    sourceNode: 'Access Policy Engine',
    affectedServices: ['Warehouse System (WMS)', 'Fleet Dispatch Portal'],
    disruptionLevel: 'High',
    tagColor: '#E5AE52',
    narrative: 'A mid-day policy sync drifted rule WS-POLICY-001 from ALLOW to DENY, blocking warehouse operators and fleet dispatchers without human sign-off.',
    rootCause: 'Silent ABAC attribute expression change evaluated during routine automated deployment.',
  },
  {
    id: 'idp_partition',
    badge: 'Federation Gateway',
    title: 'Primary IdP SAML Assertion Partition',
    sourceNode: 'Primary Identity Provider',
    affectedServices: ['Order Management', 'Warehouse System (WMS)', 'Fleet Dispatch Portal'],
    disruptionLevel: 'Critical',
    tagColor: '#E66E73',
    narrative: 'Signing certificate rollover latency partitioned downstream operational applications from root federated claims.',
    rootCause: 'Cryptographic assertion signing key expiration combined with upstream gateway rate limits.',
  },
  {
    id: 'token_flood',
    badge: 'OAuth2 / OIDC Bus',
    title: 'OAuth Token Flood & Queue Starvation',
    sourceNode: 'Order Management',
    affectedServices: ['Order Management'],
    disruptionLevel: 'Medium',
    tagColor: '#36C995',
    narrative: 'Exponential client retry loops following an upstream assertion hiccup caused token endpoint starvation, freezing order processing queues.',
    rootCause: 'Non-idempotent client retry storm flooding OAuth /token authorization server endpoints.',
  },
  {
    id: 'dag_cascade',
    badge: 'Multi-Hop Identity DAG',
    title: 'Non-Linear Dependency Deadlock',
    sourceNode: 'Recovery Controller',
    affectedServices: ['Fleet Dispatch Portal', 'Warehouse System (WMS)'],
    disruptionLevel: 'High',
    tagColor: '#E5AE52',
    narrative: 'An outage in a shared permission group cascaded across middleware scopes and service accounts in an unexpected topological sequence.',
    rootCause: 'Circular attribute dependency between dispatch worker pools and warehouse pick validation rules.',
  },
];

interface WorkflowStage {
  id: string;
  name: string;
  icon: React.ElementType;
  badge: string;
  summary: string;
  col1: { title: string; desc: string };
  col2: { title: string; desc: string };
  col3: { title: string; desc: string };
  col4: { title: string; desc: string };
}

const WORKFLOW_STAGES: WorkflowStage[] = [
  {
    id: '01',
    name: 'DETECT',
    icon: Radar,
    badge: 'Active Monitoring (300s) ● Live',
    summary: 'Identify identity authentication anomalies, policy drift across enterprise directories in real time.',
    col1: { title: '01. INGEST', desc: 'SAML assertions, OAuth/OIDC failures, directory access logs.' },
    col2: { title: '02. ANALYZE', desc: 'Detect anomalies, policy drifts, and access pattern deviations.' },
    col3: { title: '03. CORRELATE', desc: 'Map to affected services and business operations.' },
    col4: { title: '04. CLASSIFY', desc: 'Assign risk level and trigger investigation agents.' },
  },
  {
    id: '02',
    name: 'INVESTIGATE',
    icon: Search,
    badge: 'Nemotron Multi-Hop Agent',
    summary: 'Autonomous root-cause tracing across federated directories, IAM event buses, and policy repositories.',
    col1: { title: '01. PARSE DIFFS', desc: 'Cross-reference Okta/Azure change logs against historical rules.' },
    col2: { title: '02. TRAVERSE DAG', desc: 'Trace graph dependencies to identify anomalous configuration nodes.' },
    col3: { title: '03. ISOLATE ROOT', desc: 'Determine rule WS-POLICY-001 drifted from ALLOW to DENY.' },
    col4: { title: '04. CONFIDENCE', desc: 'Evaluate causal probability (0.98 diagnostic confidence score).' },
  },
  {
    id: '03',
    name: 'REASON',
    icon: Cpu,
    badge: 'NVIDIA Nemotron Super-49B',
    summary: 'Formal reasoning across threat models, compliance rules, and operational business dependencies.',
    col1: { title: '01. CONSTRAINTS', desc: 'Verify zero-trust guardrails and compliance baseline requirements.' },
    col2: { title: '02. WEIGH PATHS', desc: 'Evaluate minimal-change rollback vs hotfix assertion token.' },
    col3: { title: '03. RISK SCORING', desc: 'Calculate disruption index and blast radius for candidate fixes.' },
    col4: { title: '04. SELECT PLAYBOOK', desc: 'Select deterministic atomic rollback with scoped guardrails.' },
  },
  {
    id: '04',
    name: 'PLAN',
    icon: Box,
    badge: 'Digital Twin Sandbox Twin',
    summary: 'Dry-run proposed recovery playbooks in an isolated identity sandbox twin before execution.',
    col1: { title: '01. CLONE TWIN', desc: 'Spin up air-gapped container replica of enterprise directory state.' },
    col2: { title: '02. INJECT PATCH', desc: 'Apply candidate policy patch in isolated simulation environment.' },
    col3: { title: '03. TEST TOKENS', desc: 'Replay synthetic login transactions across downstream services.' },
    col4: { title: '04. PASS PROOF', desc: 'Verify 0% disruption score and 100% simulated access restoration.' },
  },
  {
    id: '05',
    name: 'AUTHORIZE',
    icon: Lock,
    badge: 'Cryptographic Dual-Custody',
    summary: 'Enforce cryptographic human-in-the-loop authorization before any potentially disruptive action.',
    col1: { title: '01. DOSSIER', desc: 'Generate complete Nemotron reasoning trace and verification evidence.' },
    col2: { title: '02. CHALLENGE', desc: 'Require FIDO2 / WebAuthn cryptographic approval challenge.' },
    col3: { title: '03. DUAL-SIGN', desc: 'Collect multi-party senior operator signatures for sensitive actions.' },
    col4: { title: '04. IMMUTABLE LOG', desc: 'Record cryptographic signature on append-only audit ledger.' },
  },
  {
    id: '06',
    name: 'RECOVER',
    icon: RefreshCw,
    badge: 'Deterministic Orchestrator',
    summary: 'Orchestrate deterministic remediation actions across federated identity providers and caches.',
    col1: { title: '01. ATOMIC PATCH', desc: 'Apply targeted policy reversion via verified IdP management APIs.' },
    col2: { title: '02. FLUSH CACHE', desc: 'Purge stale negative authorization decision cache entries.' },
    col3: { title: '03. RESTORE FLOW', desc: 'Re-enable assertion token exchange for isolated services.' },
    col4: { title: '04. TOPOLOGY SYNC', desc: 'Validate all downstream edge nodes transition to operational.' },
  },
  {
    id: '07',
    name: 'VERIFY',
    icon: ShieldCheck,
    badge: 'Dual-Assertion Verification',
    summary: 'Conduct independent cryptographic access verification across multiple trust paths.',
    col1: { title: '01. TEST ASSERTIONS', desc: 'Execute live synthetic logins across all recovered service endpoints.' },
    col2: { title: '02. ZERO-TRUST CHECK', desc: 'Verify no unintended permissions or bypasses were granted.' },
    col3: { title: '03. LATENCY CHECK', desc: 'Measure authentication round-trip latency against baseline SLA.' },
    col4: { title: '04. CLOSE TICKET', desc: 'Issue cryptographic post-incident report and seal audit trail.' },
  },
];
"""

with open("/Users/krishnavarshithkamanaboina/Desktop/Nvidia/part1.py", "w") as f:
    f.write(part1)

print("Part 1 written successfully!")

